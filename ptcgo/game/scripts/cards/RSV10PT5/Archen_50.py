from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="57d4a95c-970c-5ad6-8e0c-e7e8a14a2423",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    display_name="Archen",
    searchable_by=["Archen", "Stage 1", "Archen"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AntiuqePlumeFossil.Name",
    family_id=566,
    abilities=[
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)