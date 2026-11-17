from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="830b7a2a-2bde-5695-a222-c783467fa64a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "GenesectEX"],
    subtypes=["Basic", "EX"],
    collector_number=64,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=649,
    abilities=[
        Ability(
            title="Drive Change",
            game_text="Once during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to this Pok\u00e9mon into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Rapid Blaster",
            game_text="Discard as many Metal Energy attached to this Pok\u00e9mon as you like. This attack does 20 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.METAL: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)