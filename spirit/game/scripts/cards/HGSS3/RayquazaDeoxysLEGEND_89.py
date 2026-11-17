from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5eecf87e-d3e1-5c81-acb2-cb26b76b81bb",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaDeoxysLEGEND.Name",
    display_name="Rayquaza & Deoxys LEGEND",
    searchable_by=["Rayquaza & Deoxys LEGEND", "LEGEND", "RayquazaDeoxysLEGEND"],
    subtypes=["LEGEND"],
    collector_number=89,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.COLORLESS, PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=384,
    abilities=[
        Ability(
            title="Space Virus",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from an attack of Rayquaza & Deoxys LEGEND, take 1 more Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Ozone Buster",
            game_text="Discard all Fire Energy attached to Rayquaza & Deoxys LEGEND.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)