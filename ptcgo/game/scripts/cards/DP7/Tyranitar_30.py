from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16d9ada8-a333-5772-af8d-240541fd08ff",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Darkness Drive",
            game_text="After your opponent's Pok\u00e9mon uses a Pok\u00e9-Power, you may search your discard pile for a basic Darkness Energy card and attach it to Tyranitar.",
            effect=unimplemented,
        ),
        Attack(
            title="Grind",
            game_text="Does 20 damage times the amount of Energy attached to Tyranitar.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Tail",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 5},
            effect=unimplemented,
        ),
    ],
)