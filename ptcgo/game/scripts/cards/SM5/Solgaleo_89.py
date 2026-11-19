from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e19ba5d0-52ba-5cee-8118-9660c7dd2974",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name",
    display_name="Solgaleo ◇",
    searchable_by=["Solgaleo \u25c7", "Basic", "Prism Star", "Solgaleo"],
    subtypes=["Basic", "Prism Star"],
    collector_number=89,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=791,
    abilities=[
        Attack(
            title="Radiant Star",
            game_text="For each of your opponent's Pok\u00e9mon in play, attach a Metal Energy card from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.METAL: 1},
            effect=lock_self_attack(),
        ),
        Attack(
            title="Corona Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.METAL: 4},
            damage=160,
            effect=unimplemented,
        ),
    ],
)