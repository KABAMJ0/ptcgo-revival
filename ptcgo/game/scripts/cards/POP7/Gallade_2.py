from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e38d3357-62d4-5056-a00e-f3048d9ab02d",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gallade.Name",
    display_name="Gallade",
    searchable_by=["Gallade", "Stage 2", "Gallade"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="POP7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Sonic Blade",
            game_text="Put damage counters on the Defending Pok\u00e9mon until it is 50 HP away from being Knocked Out. If you do, your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Cut",
            game_text="You may choose as many of your face-down Prize cards as you like and put them face up. If you do, this attack does 60 damage plus 20 more damage for each Prize card you chose. (These cards remain face up for the rest of the game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)