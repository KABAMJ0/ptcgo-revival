from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="569ff88d-5d74-5cc6-8aed-c8ac0c08d2ef",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic", "Magearna"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=801,
    abilities=[
        Ability(
            title="Auto Heal",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever you attach an Energy card from your hand to 1 of your Pok\u00e9mon, heal 90 damage from that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)