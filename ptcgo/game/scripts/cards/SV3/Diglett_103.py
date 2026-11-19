from ptcgo.game.card_effects.support_common import bare_mill
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import bare_mill

card = PokemonCardDef(
    guid="b85c96f2-ea13-5402-a54f-ce50edba3303",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic", "Diglett"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Hole-Diggin' Noggin",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=bare_mill(1, opponent=False),
        ),
    ],
)