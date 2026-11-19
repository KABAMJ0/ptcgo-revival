from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6230fe74-10ce-5ca5-a30e-f7d21837a1cf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensSkwovet.Name",
    display_name="Arven's Skwovet",
    searchable_by=["Arven's Skwovet", "Basic", "ArvensSkwovet"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Gnaw Through",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=discard_defender_tools_then_damage(),
        ),
    ],
)