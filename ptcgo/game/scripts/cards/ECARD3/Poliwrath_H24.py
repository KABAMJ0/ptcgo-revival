from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot, unafflicted
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

def _strange_spiral_ready(board, player_id, pokemon) -> bool:
    return (is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)
            and any(is_basic_energy_card(e) for e in board.attached_energies(pokemon)))


async def _strange_spiral(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_basic_energy_card, minimum=1,
        prompt="Choose a basic Energy to discard from Poliwrath")
    if discarded and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="fccab15a-4dc4-5b22-8485-a8e84f561bdf",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Strange Spiral",
            game_text="Once during your turn (before your attack), if Poliwrath is your Active Pok\u00e9mon, you may discard a basic Energy card attached to Poliwrath. If you do, the Defending Pok\u00e9mon is now Confused. This power can't be used if Poliwrath is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_strange_spiral_ready,
            effect=_strange_spiral,
        ),
        Attack(
            title="Spiral Punch",
            game_text="Flip a coin until you get tails. This attack does 40 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_damage(per_heads=20, until_tails=True, base=40),
        ),
    ],
)
