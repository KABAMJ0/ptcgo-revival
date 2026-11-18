from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04f916d4-9892-5f71-9df5-ab79a0eba266",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1", "Centiskorch"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Attack(
            title="Controlled Burn",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=recoil_attack(30),
        ),
    ],
)