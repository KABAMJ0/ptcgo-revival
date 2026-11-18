from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="814e0f07-3c59-5461-aba1-ecdace6bdbc9",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine δ",
    searchable_by=["Mantine \u03b4", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=226,
    abilities=[
        Ability(
            title="Power Circulation",
            game_text="Once during your turn (before your attack), you may search your discard pile for a basic Energy card, show it to your opponent, and put it on top of your deck. If you do, put 1 damage counter on Mantine. This power can't be used if Mantine is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 1 damage counter from Mantine.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)