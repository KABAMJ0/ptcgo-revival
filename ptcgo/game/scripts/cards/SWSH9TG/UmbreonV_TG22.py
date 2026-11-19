from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="5c00a7af-58a5-5fff-b85a-7c4ca02f3ce7",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonV.Name",
    display_name="Umbreon V",
    searchable_by=["Umbreon V", "Basic", "V", "Single Strike", "UmbreonV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=22,
    set_code="SWSH9TG",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=197,
    abilities=[
        Attack(
            title="Mean Look",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Moonlight Blade",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)