from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import Activations


async def _vacation(ctx):
    """VACATION: 2 counters off every Pokemon, and the turn ends."""
    healed = 0
    for pokemon in ctx.my_pokemon_in_play():
        healed += await ctx.heal(20, target=pokemon)
    if healed:
        ctx.ends_turn = True

card = PokemonCardDef(
    guid="61039d44-3ae7-591d-a294-715f4f711a92",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown [V]",
    searchable_by=["Unown [V]", "Basic", "UnownV"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="VACATION",
            game_text="Once during your turn (before your attack), you may remove 2 damage counters from each of your Pok\u00e9mon. If you do, your turn ends. This power can't be used if Unown V is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=_vacation,
        ),
        Attack(
            title="Hidden Power",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=spread_damage(10, side="mine"),
        ),
    ],
)