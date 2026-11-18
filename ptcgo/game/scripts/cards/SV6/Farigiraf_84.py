from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4858d76-67ae-56c6-ac68-c78fb92fd6d1",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigiraf.Name",
    display_name="Farigiraf",
    searchable_by=["Farigiraf", "Stage 1", "Farigiraf"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Attack(
            title="One-derful Rumble",
            game_text="This attack does 40 damage for each of your Stage 1 Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)