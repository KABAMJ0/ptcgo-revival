from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcc75a0d-6027-55c0-b795-783fb8ef057e",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durantex.Name",
    display_name="Durant ex",
    searchable_by=["Durant ex", "Basic", "ex", "Durantex"],
    subtypes=["Basic", "ex"],
    collector_number=215,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=632,
    abilities=[
        Ability(
            title="Sudden Shearing",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard the top card of your opponent's deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Vengeful Crush",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)