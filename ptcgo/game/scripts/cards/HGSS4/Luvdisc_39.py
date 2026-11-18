from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="17fbdb52-c9b9-5d07-a7c1-a83557cb9c19",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Rendezvous Draw",
            game_text="Each player draws and reveals the top card of his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Distorted Wave",
            game_text="Before doing damage, remove 1 damage counter from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)