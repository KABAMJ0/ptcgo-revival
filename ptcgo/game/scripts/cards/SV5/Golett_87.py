from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="3699db37-7e7e-5884-b7e7-3c688a989259",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic", "Golett"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=622,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)