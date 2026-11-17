from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="692f9def-80ba-541d-980a-6225baeed84b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansTyphlosion.Name",
    display_name="Ethan's Typhlosion",
    searchable_by=["Ethan's Typhlosion", "Stage 2", "EthansTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=190,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansQuilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Buddy Blast",
            game_text="This attack does 60 more damage for each Ethan's Adventure card in your discard pile.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)