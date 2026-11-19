from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_pokemon_ex

class _RearSensorLock(Passive):
    """Each player's Active Basic Pokemon (excluding Pokemon-ex) can't use
    Poke-Powers."""

    def blocks_abilities(self, pokemon, carrier):
        return (is_in_active_spot(pokemon)
                and pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
                and not is_pokemon_ex(pokemon))


async def foresight(ctx):
    """Look at the top 5 cards of either deck and put them back in any order."""
    options = ["Your deck", "Your opponent's deck"]
    chosen = await ctx.choose("Rearrange the top 5 cards of which deck?", options)
    player_id = ctx.player_id if chosen == 0 else ctx.opponent_id
    await ctx.reorder_deck_top(5, player_id=player_id,
                               prompt="Rearrange the top 5 cards of that deck")


card = PokemonCardDef(
    guid="c8737ac4-fb67-51d8-a1fa-e0e8cecf2a66",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Ability(
            title="Rear Sensor",
            game_text="Each player's Active Basic Pok\u00e9mon (excluding Pok\u00e9mon-ex) can't use any Pok\u00e9-Powers.",
            passive=_RearSensorLock(),
        ),
        Attack(
            title="Foresight",
            game_text="Look at the top 5 cards on either player's deck and put them back on top of that player's deck in any order you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=foresight,
        ),
        Attack(
            title="Disorder",
            game_text="If the Defending Pok\u00e9mon has any Special Energy cards attached to it, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)