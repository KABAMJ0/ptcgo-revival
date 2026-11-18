from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="bde4995f-40fb-549b-8ba5-867874badde8",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1", "Palafin"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Vanguard Punch",
            game_text="This Pok\u00e9mon also does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.WATER: 1},
            damage=130,
            effect=unimplemented,
        ),
        Attack(
            title="Double Hit",
            game_text="Flip 2 coins. This attack does 90 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=90),
        ),
    ],
)