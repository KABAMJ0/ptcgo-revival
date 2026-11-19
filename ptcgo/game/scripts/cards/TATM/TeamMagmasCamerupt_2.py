from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_fire_energy, is_fighting_energy
from ptcgo.game.card_effects.support_common import (
    attach_from_discard, requires_discard,
)
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _is_fire_or_fighting_energy(card) -> bool:
    return is_fire_energy(card) or is_fighting_energy(card)


async def _hurricane(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        await ctx.move_energy_freely(
            [ctx.attacker], bench, predicate=is_basic_energy_card, max_count=1,
            prompt="Choose a basic Energy to move to a Benched Pokémon",
        )


card = PokemonCardDef(
    guid="2a196ea2-1d25-5a3a-a9a5-d18bc8146e2d",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasCamerupt.Name",
    display_name="Team Magma's Camerupt",
    searchable_by=["Team Magma's Camerupt", "Stage 1", "TeamMagmasCamerupt"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Burning Draft",
            game_text="Once during your turn (before your attack), you may attach a Fighting or Fire Energy card from your discard pile to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_discard(_is_fire_or_fighting_energy, 1),
            effect=attach_from_discard(
                predicate=_is_fire_or_fighting_energy, count=1, target="self",
                prompt="Choose a Fighting or Fire Energy card to attach"),
        ),
        Attack(
            title="Flame Ball",
            game_text="Move a basic Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_hurricane,
        ),
    ],
)
