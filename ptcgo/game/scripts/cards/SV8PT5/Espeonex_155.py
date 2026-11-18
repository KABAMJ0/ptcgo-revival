from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be61c437-120c-5e64-bb0c-7b4ff73130bd",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name",
    display_name="Espeon ex",
    searchable_by=["Espeon ex", "Stage 1", "Tera", "ex", "Espeonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=155,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Psych Out",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
        Attack(
            title="Amazez",
            game_text="Devolve each of your opponent's evolved Pok\u00e9mon by shuffling the highest Stage Evolution card on it into your opponent's deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)