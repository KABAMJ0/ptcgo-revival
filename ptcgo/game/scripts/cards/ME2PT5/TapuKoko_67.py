from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53a70781-b89a-54f7-936e-96ffd211a0a4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKoko.Name",
    display_name="Tapu Koko",
    searchable_by=["Tapu Koko", "Basic", "TapuKoko"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Fast Flight",
            game_text="If you go first, you can use this attack during your first turn. Discard your hand and draw 5 cards.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)