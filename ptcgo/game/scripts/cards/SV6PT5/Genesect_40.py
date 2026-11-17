from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a527118a-db3c-5284-b61d-7ce43593510b",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic", "Genesect"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=649,
    abilities=[
        Ability(
            title="ACE Nullifier",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, your opponent can't play any ACE SPEC cards from their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Magnetic Blast",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)