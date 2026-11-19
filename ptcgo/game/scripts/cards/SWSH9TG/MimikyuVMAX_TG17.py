from ptcgo.game.card_effects.attacks_common import discard_random_hand_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c589b235-5c47-55ce-940c-b4a8181eaa72",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuVMAX.Name",
    display_name="Mimikyu VMAX",
    searchable_by=["Mimikyu VMAX", "VMAX", "MimikyuVMAX"],
    subtypes=["VMAX"],
    collector_number=17,
    set_code="SWSH9TG",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuV.Name",
    family_id=778,
    abilities=[
        Attack(
            title="Ominous Numbers",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like. If you played Acerola's Premonition from your hand during this turn, place 13 damage counters instead.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Max Shadow",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=discard_random_hand_attack(1),
        ),
    ],
)