from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d607eba-0baf-55b9-b89f-435f93c29aa3",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic", "Tornadus"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Attack(
            title="Wrapped in Wind",
            game_text="Attach a Basic Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(is_basic_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Hurricane",
            game_text="Move a Basic Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)