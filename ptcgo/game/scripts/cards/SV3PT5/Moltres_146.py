from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58a8ce0a-02a7-549a-abfd-67e4f7c85158",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Ability(
            title="Flare Float",
            game_text="If this Pok\u00e9mon has any Fire Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Blazing Flight",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 3},
            effect=unimplemented,
        ),
    ],
)