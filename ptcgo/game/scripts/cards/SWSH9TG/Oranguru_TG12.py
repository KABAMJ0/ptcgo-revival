from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import primate_wisdom
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
card = PokemonCardDef(
    guid="2b191c7b-b3e9-5125-811f-a95057813806",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic", "Oranguru"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Ability(
            title="Primate Wisdom",
            game_text="Once during your turn, you may switch a card from your hand with the top card of your deck.",
            effect=primate_wisdom,
        ),
        Attack(
            title="Whap Down",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)