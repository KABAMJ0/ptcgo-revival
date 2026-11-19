from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import cure_on_energy_attach
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _burn_booster(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, prompt="Discard an Energy card attached to Flareon")
    if not discarded:
        return
    bonus = 10 if energy_provides_type(discarded[0], PokemonTypes.FIRE.value) else 0
    await ctx.deal_damage(40 + bonus)


card = PokemonCardDef(
    guid="38ab1fe2-3f7c-59da-98d1-5efb36f96641",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Self-healing",
            game_text="Whenever you attach a Fire Energy card from your hand to Flareon, remove all Special Conditions affecting Flareon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=cure_on_energy_attach(PokemonTypes.FIRE),
        ),
        Attack(
            title="Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Burn Booster",
            game_text="Discard an Energy card attached to Flareon in order to use this attack. If the discarded card is a Fire Energy card, this attack does 40 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=_burn_booster,
        ),
    ],
)