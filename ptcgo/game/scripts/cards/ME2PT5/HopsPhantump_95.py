from ptcgo.game.card_effects.passives_common import flip_protection
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccac9b67-6b53-5e16-a3d0-2f3548ceeb92",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsPhantump.Name",
    display_name="Hop's Phantump",
    searchable_by=["Hop's Phantump", "Basic", "HopsPhantump"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=708,
    abilities=[
        Attack(
            title="Splashing Dodge",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)