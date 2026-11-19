from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import (
    attach_from_discard, requires_bench_space,
)


def _darkness_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.DARKNESS.value)


async def restoration(ctx):
    """From the discard pile onto your Bench, then attach a Darkness Energy
    card from the discard pile to it."""
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    await attach_from_discard(_darkness_energy, count=1, target="self",
                              minimum=0)(ctx)


card = PokemonCardDef(
    guid="693b1852-448e-5261-b632-de7838bde5b0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiGX.Name",
    display_name="Darkrai-GX",
    searchable_by=["Darkrai-GX", "Basic", "GX", "DarkraiGX"],
    subtypes=["Basic", "GX"],
    collector_number=158,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Ability(
            title="Restoration",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. Then, attach a Darkness Energy card from your discard pile to this Pok\u00e9mon.",
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_bench_space(1),
            effect=restoration,
        ),
        Attack(
            title="Dark Cleave",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
        Attack(
            title="Dead End-GX",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, that Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)