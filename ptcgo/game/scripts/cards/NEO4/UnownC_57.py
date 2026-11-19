from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.session.passives import Passive


class ChasePassive(Passive):
    """Whenever the OPPONENT's Active tries to retreat, flip a coin; on heads it
    takes a damage counter (Weakness and Resistance apply)."""

    async def on_retreat(self, ctx, pokemon, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return
        heads = await ctx.flip_coins(1, "Chase")
        if heads and heads[0]:
            await ctx.deal_damage(10, target=pokemon)


def _chase():
    """As long as Unown [C] is Active, a retreating opponent's Active takes 1
    damage counter on a heads flip."""
    return ChasePassive()


card = PokemonCardDef(
    guid="8b54f2e4-2ba9-5651-b7ce-8c26ec2963ce",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownC.Name",
    display_name="Unown [C]",
    searchable_by=["Unown [C]", "Basic", "UnownC"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Chase]",
            game_text="As long as Unown [C] is your Active Pok\u00e9mon, whenever your opponent's Active Pok\u00e9mon tries to retreat, flip a coin. If heads, put 1 damage counter on that Pok\u00e9mon. Apply Weakness and Resistance.",
            passive=_chase(),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)