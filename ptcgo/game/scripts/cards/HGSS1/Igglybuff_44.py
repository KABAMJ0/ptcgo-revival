from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6652da20-3cc6-5700-a22b-46dadd85cc1b",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Basic", "Igglybuff"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=174,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Igglybuff is Asleep, prevent all damage done to Igglybuff by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Graffiti",
            game_text="Igglybuff is now Asleep. During your opponent's next turn, the attack cost of each of the Defending Pok\u00e9mon's attacks is Colorless more.",
            cost={},
            effect=unimplemented,
        ),
    ],
)