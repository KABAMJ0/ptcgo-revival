from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3088714e-2d97-5bb8-9468-1b1aadc14ec9",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Arm Thrust Practice",
            game_text="All of your Pok\u00e9mon take 10 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Rocket Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)