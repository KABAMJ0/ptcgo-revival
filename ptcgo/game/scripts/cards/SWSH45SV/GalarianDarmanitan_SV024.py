from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="b615897f-9f98-5eae-b6af-5e6cc0bba8ad",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitan.Name",
    display_name="Galarian Darmanitan",
    searchable_by=["Galarian Darmanitan", "Stage 1", "GalarianDarmanitan"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
        Attack(
            title="Crushing Headbutt",
            game_text="During your next turn, this Pok\u00e9mon can't use Crushing Headbutt.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)