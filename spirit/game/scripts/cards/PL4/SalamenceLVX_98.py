from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c470a2c-56df-5b79-a417-ec5b67c4ff4f",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceLVX.Name",
    display_name="Salamence LV.X",
    searchable_by=["Salamence LV.X", "Level-Up", "SalamenceLVX"],
    subtypes=["Level-Up"],
    collector_number=98,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Double Fall",
            game_text="Once during your turn (before your attack), when you put Salamence LV.X from your hand onto your Active Salamence, you may use this power. For each of your opponent's Pok\u00e9mon that is Knocked Out by damage from Salamence's attacks this turn, take 1 more Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Steam Blast",
            game_text="Discard an Energy card attached to Salamence.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)