from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e0ca2194-39cb-50ec-b7f7-f29c6f38d5c4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BruteBonnet.Name",
    display_name="Brute Bonnet",
    searchable_by=["Brute Bonnet", "Basic", "Ancient", "BruteBonnet"],
    subtypes=["Basic", "Ancient"],
    collector_number=207,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=986,
    abilities=[
        Ability(
            title="Toxic Powder",
            game_text="Once during your turn, if this Pok\u00e9mon has an Ancient Booster Energy Capsule attached, you may make both Active Pok\u00e9mon Poisoned.",
            effect=unimplemented,
        ),
        Attack(
            title="Rampaging Hammer",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)