from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b0169faf-989c-509a-9d2c-a419f0ad9518",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mausholdex.Name",
    display_name="Maushold ex",
    searchable_by=["Maushold ex", "Stage 1", "ex", "Mausholdex"],
    subtypes=["Stage 1", "ex"],
    collector_number=155,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Ability(
            title="Solidarity",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon for each of your Tandemaus, Maushold, and Maushold ex in play.",
            effect=unimplemented,
        ),
        Attack(
            title="Nom-Nom-Nom Incisors",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)