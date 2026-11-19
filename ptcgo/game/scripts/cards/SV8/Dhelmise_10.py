from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage

card = PokemonCardDef(
    guid="c5875967-a667-54e4-a574-a2e0d6ac5c56",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Rescue Kedge",
            game_text="Put up to 2 Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Annihilating Anchor",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=discard_defender_tools_then_damage(),
        ),
    ],
)