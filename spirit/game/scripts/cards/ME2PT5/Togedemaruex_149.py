from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59854994-7efb-590d-a34e-d9762335d4eb",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaruex.Name",
    display_name="Togedemaru ex",
    searchable_by=["Togedemaru ex", "Basic", "ex", "Togedemaruex"],
    subtypes=["Basic", "ex"],
    collector_number=149,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=777,
    abilities=[
        Attack(
            title="Stun Needle",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Spiky Rolling",
            game_text="If this Pok\u00e9mon used Spiky Rolling during your last turn, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)