from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def thunderspark(ctx):
    """10 to every Benched Pokemon on either side that has Energy attached."""
    for side in (ctx.my_bench(), ctx.opponent_bench()):
        for target in side:
            if ctx.attached_energies(target):
                await ctx.deal_damage(10, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="52c00b0e-7c65-533e-b315-aeb74d673c53",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasManectric.Name",
    display_name="Team Aqua's Manectric",
    searchable_by=["Team Aqua's Manectric", "Stage 1", "TeamAquasManectric"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasElectrike.Name",
    family_id=309,
    abilities=[
        Ability(
            title="Power Shift",
            game_text="Once during your turn (before your attack), you may move any number of basic Energy cards attached to 1 of your Pok\u00e9mon with Team Aqua in its name to another of your Pok\u00e9mon. This power can't be used if Team Aqua's Manectric is affected by a Special Condition.",
            effect=move_energy_between(is_basic_energy_card, count=None, prompt="Move any number of basic Energy cards"),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Thunderspark",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's) that has Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=thunderspark,
        ),
    ],
)