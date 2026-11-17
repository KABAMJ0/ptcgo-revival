from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d997fe4-ea63-5a81-939a-d9ca381b5882",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Yank Away",
            game_text="Choose 2 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)