from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4055537d-8582-5f83-83c6-f7168441c49e",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    display_name="Carvanha",
    searchable_by=["Carvanha", "Basic", "Carvanha"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If Carvanha is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Carvanha is Knocked Out), put 1 damage counter on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Big Bite",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=no_retreat_attack(),
        ),
    ],
)