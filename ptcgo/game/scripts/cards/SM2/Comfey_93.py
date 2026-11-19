from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.passives_common import ConditionImmunityPassive
from ptcgo.game.card_effects.pokemon import energy_provides_type

def _my_fairy_pokemon(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(child, PokemonTypes.FAIRY.value)
               for child in target.children)


class FlowerShieldPassive(ConditionImmunityPassive):
    """My Pokemon holding Fairy Energy cannot be affected by any condition."""

    def __init__(self):
        super().__init__(None, _my_fairy_pokemon)


async def _flower_shield_enter(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if _my_fairy_pokemon(pokemon, ctx.source):
            await ctx.cure_all_conditions(pokemon)


card = PokemonCardDef(
    guid="21fcddc6-697c-5923-b9b1-3d7e21e78f49",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic", "Comfey"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=764,
    abilities=[
        Ability(
            title="Flower Shield",
            game_text="Each of your Pok\u00e9mon that has any Fairy Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pok\u00e9mon.",
            passive=FlowerShieldPassive(),
            trigger=Triggers.ON_PLAY,
            effect=_flower_shield_enter,
        ),
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent draws a card.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)