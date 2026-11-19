from ptcgo.game.card_effects.attacks_common import flip_damage, ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd9d2679-2378-5eb0-a7be-c118d3f08e66",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2", "Conkeldurr"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Chip Away",
            game_text="This attack's damage isn't affected by any effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)