from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb547988-9487-5efe-bbc5-a91613c06567",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizorex.Name",
    display_name="Scizor ex",
    searchable_by=["Scizor ex", "Stage 1", "ex", "Scizorex"],
    subtypes=["Stage 1", "ex"],
    collector_number=111,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Cross Breaker",
            game_text="Discard up to 2 Metal Energy from this Pok\u00e9mon. This attack does 120 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)