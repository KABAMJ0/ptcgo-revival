from ptcgo.game.card_effects.support_common import gust_then
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _burn_new_defender(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="140e4025-a3a1-5cf7-b0e2-441cccdd9cb0",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Luring Flame",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. The new Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=gust_then(_burn_new_defender),
        ),
        Attack(
            title="Fiery Licks",
            game_text="Discard the top 4 cards of your deck. This attack does 50 damage times the number of Fire Energy cards discarded.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            damage_operator="x",
            effect=mill_scaled_damage(
                4, 50,
                pred=lambda card: energy_provides_type(
                    card, PokemonTypes.FIRE.value
                ),
            ),
        ),
    ],
)