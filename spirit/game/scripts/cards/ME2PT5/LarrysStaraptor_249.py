from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58bdcce9-08bc-5d7b-9db9-b5ccdb9e10de",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStaraptor.Name",
    display_name="Larry's Staraptor",
    searchable_by=["Larry's Staraptor", "Stage 2", "LarrysStaraptor"],
    subtypes=["Stage 2"],
    collector_number=249,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStaravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Facade",
            game_text="If this Pok\u00e9mon is Burned or Poisoned, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Feathery Strike",
            game_text="Discard 2 Energy from this Pok\u00e9mon, and this attack also does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)