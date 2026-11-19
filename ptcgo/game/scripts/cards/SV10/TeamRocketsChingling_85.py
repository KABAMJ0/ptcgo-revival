from ptcgo.game.card_effects.attacks_common import discard_random_hand_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6494ccc1-7a77-50f6-a29e-a48321ffdfd1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsChingling.Name",
    display_name="Team Rocket's Chingling",
    searchable_by=["Team Rocket's Chingling", "Basic", "TeamRocketsChingling"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=433,
    abilities=[
        Attack(
            title="Chiming Commotion",
            game_text="Discard a random card from your opponent's hand.",
            cost={},
            effect=discard_random_hand_attack(1),
        ),
    ],
)