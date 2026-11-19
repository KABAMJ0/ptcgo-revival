from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="3dba6b17-4b65-54b6-9595-83797623111c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic", "Tornadus"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Ability(
            title="Incarnate Solidarity",
            game_text="If you have Tornadus, Thundurus, Landorus, and Enamorus in play, ignore all Colorless Energy in the costs of attacks used by this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Corkscrew Dive",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=draw_until_effect(6),
        ),
    ],
)