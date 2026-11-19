from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                   SpecialConditions)
from ptcgo.game.card_effects.support_common import gust_then
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack

async def _tri_hazard(ctx, new_active):
    for condition in (SpecialConditions.BURNED, SpecialConditions.PARALYZED,
                      SpecialConditions.POISONED):
        await ctx.apply_special_condition(new_active, condition)

card = PokemonCardDef(
    guid="df860e71-0153-55c1-abf7-b8225be909be",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMukGX.Name",
    display_name="Alolan Muk-GX",
    searchable_by=["Alolan Muk-GX", "Stage 1", "GX", "AlolanMukGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=84,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Chemical Breath",
            game_text="This attack does 70 more damage for each Special Condition affecting your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Tri Hazard-GX",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Burned, Paralyzed, and Poisoned. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=gust_then(_tri_hazard),
        ),
    ],
)