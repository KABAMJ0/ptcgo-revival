from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="07b0c2f1-ddce-5a3e-9184-17746aaee251",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsLarvitar.Name",
    display_name="Team Rocket's Larvitar",
    searchable_by=["Team Rocket's Larvitar", "Basic", "TeamRocketsLarvitar"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=246,
    abilities=[
        Attack(
            title="Mountain Munch",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=mill_attack(1, opponent=True),
        ),
    ],
)