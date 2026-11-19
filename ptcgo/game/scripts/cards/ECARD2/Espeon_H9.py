from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.support_common import return_attached_energy
from ptcgo.game.attributes import AttrID


def _energy_to_return(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    return any(board.attached_energies(p) for p in board.pokemon_in_play(player_id))


async def _damage_blast(ctx):
    defender = ctx.defender
    counters = 0
    if defender is not None:
        counters = max(0, (ctx.max_hp(defender) - defender.get_attribute(AttrID.HP, 0)) // 10)
    heads = 0
    if counters:
        results = await ctx.flip_coins(counters, "Damage Blast")
        heads = sum(1 for result in results if result)
    await ctx.deal_damage(30 + 10 * heads)


card = PokemonCardDef(
    guid="2f5b2236-a458-5e99-bb1d-afe398ee3db9",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Energy Return",
            game_text="As often as you like during your turn (before your attack), choose an Energy card attached to 1 of your Pok\u00e9mon and return it to your hand. This power can't be used if Espeon is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_energy_to_return,
            effect=return_attached_energy(count=1, target="choice", to="hand"),
        ),
        Attack(
            title="Damage Blast",
            game_text="Flip a number of coins equal to the number of damage counters on the Defending Pok\u00e9mon. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)